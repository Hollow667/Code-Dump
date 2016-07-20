package com.hivemind.zerodavila.texttransferactivitiesexample;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
    }

    public void showMessage(View v) {
        Bundle bundle = getIntent().getExtras();
        String message = bundle.getString("send_data");
        Toast.makeText(getBaseContext(), "Message : " + message,
                Toast.LENGTH_SHORT).show();
    }
}
