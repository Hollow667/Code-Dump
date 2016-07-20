package com.hivemind.zerodavila.listitemmanipulation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    ListView lv;
    EditText nameTxt;
    Button addBtn, updateBtn, delBtn, clearBtn;
    ArrayList<String> names=new ArrayList<String>();
    ArrayAdapter<String> adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        lv = (ListView) findViewById(R.id.listView);
        nameTxt = (EditText) findViewById(R.id.textField);
        addBtn = (Button) findViewById(R.id.addButton);
        updateBtn = (Button) findViewById(R.id.updateButton);
        delBtn = (Button) findViewById(R.id.delButton);
        clearBtn = (Button) findViewById(R.id.clearButton);

        //ADAPTER
        adapter = new ArrayAdapter<String>(this, android.R.layout.select_dialog_singlechoice, names);
        lv.setAdapter(adapter);

        //SET SELECTED ITEM
        lv.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> arg0, View v, int pos, long id) {
                //TODO
                nameTxt.setText(names.get(pos));

            }
        });

        //HANDLE EVENTS
        addBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                add();
            }
        });

        updateBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                update();
            }
        });

        delBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                delete();
            }
        });

        clearBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                clear();
            }
        });
    }

    //ADD
    private void add() {
        String name = nameTxt.getText().toString();

        if(!name.isEmpty() && name.length() > 0) {
            //ADD
            adapter.add(name);

            //REFRESH
            adapter.notifyDataSetChanged();

            nameTxt.setText("");

            Toast.makeText(getApplicationContext(), "Added " + name, Toast.LENGTH_SHORT).show();
        }
    }

    //UPDATE
    private void update() {
        String name=nameTxt.getText().toString();

        //GET POS OF SELECTED ITEM
        int pos = lv.getCheckedItemPosition();

        if(!name.isEmpty() && name.length() > 0) {
            //REMOVE ITEM
            adapter.remove(names.get(pos));

            //INSERT
            adapter.insert(name, pos);

            //REFRESH
            adapter.notifyDataSetChanged();

            Toast.makeText(getApplicationContext(), "Updated " + name,
                    Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(getApplicationContext(), "!! Nothing to update",
                    Toast.LENGTH_SHORT).show();
        }
    }

    //DELETE
    private void delete() {
        int pos = lv.getCheckedItemPosition();

        if(pos > -1) {
            //REMOVE
            adapter.remove(names.get(pos));

            //REFRESH
            adapter.notifyDataSetChanged();

            nameTxt.setText("");

            Toast.makeText(getApplicationContext(), "Deleted " ,
                    Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(getApplicationContext(), "!! Nothing to update",
                    Toast.LENGTH_SHORT).show();
        }
    }

    //CLEAR
    private void clear() {
        adapter.clear();
    }
}
