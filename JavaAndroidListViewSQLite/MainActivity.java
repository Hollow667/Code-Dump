import android.database.Cursor;
import android.support.v4.widget.SimpleCursorAdapter;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.text.format.Time;
import android.view.View;
import android.widget.AdapterView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    Time today = new Time(Time.getCurrentTimezone());
    DBAdapter myDB;
    EditText etTasks;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etTasks = (EditText) findViewById(R.id.editTextTask);
        openDB();
        populateListView();
        listViewItemClick();
        listViewItemLongClick();

    }

    private void openDB() {
        myDB = new DBAdapter(this);
        myDB.open();
    }

    public void onClick_AddTask(View v) {
        today.setToNow();
        String timeStamp = today.format("%Y-%M-%D %H:%M:%S");
        if(!TextUtils.isEmpty(etTasks.getText().toString())) {
            myDB.insertRow(etTasks.getText().toString(), timeStamp);
        }
        populateListView();
    }

    private void populateListView() {
        Cursor cursor = myDB.getAllRows();

        String[] fromFieldNames = new String[] {
                DBAdapter.KEY_ROWID,DBAdapter.KEY_TASK
        };

        int[] toViewIDs = new int[] {
                R.id.textViewItemNumber, R.id.textViewItemTask
        };

        SimpleCursorAdapter myCursorAdapter;
        myCursorAdapter = new SimpleCursorAdapter(getBaseContext(),R.layout.item_layout,cursor,fromFieldNames,toViewIDs,0);
        ListView myList = (ListView)findViewById(R.id.listViewTasks);
        myList.setAdapter(myCursorAdapter);
    }

    private void updateTask(long id) {
        Cursor cursor = myDB.getRow(id);
        if(cursor.moveToFirst()) {
            String task = etTasks.getText().toString();
            today.setToNow();
            String date = today.format("%Y-%M-%D %H:%M:%S");
            myDB.updateRow(id, task, date);
        }

        cursor.close();
    }

    private void listViewItemClick() {
        ListView myList = (ListView) findViewById(R.id.listViewTasks);
        myList.setOnItemClickListener(new AdapterView.OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int arg2, long id) {
                updateTask(id);
                populateListView();
                displayToast(id);
            }
        });
    }

    public void onClick_DeleteTasks(View v) {
        myDB.deleteAll();
        populateListView();
    }

    private void listViewItemLongClick() {
        ListView myList = (ListView) findViewById(R.id.listViewTasks);
        myList.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {

            @Override
            public boolean onItemLongClick(AdapterView<?> adapterView, View view, int i, long id) {
                myDB.deleteRow(id);
                populateListView();

                return false;
            }
        });
    }

    private void displayToast(long id) {
        Cursor cursor = myDB.getRow(id);
        if(cursor.moveToFirst()) {
            long idDB = cursor.getLong(DBAdapter.COL_ROWID);
            String task = cursor.getString(DBAdapter.COL_TASK);
            String date = cursor.getString(DBAdapter.COL_DATE);

            String message = "ID: " + idDB + "\n" + "Task: " + task + "\n" + "Date: " + date;

            Toast.makeText(MainActivity.this, message, Toast.LENGTH_LONG).show();
        }
        cursor.close();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        closeDB();
    }

    private void closeDB() {
        myDB.close();
    }
}
