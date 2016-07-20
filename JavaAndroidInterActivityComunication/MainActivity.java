package com.hivemind.zerodavila.texttransferactivitiesexample;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    Button button;
    EditText txt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button = (Button) findViewById(R.id.bn);
        txt = (EditText) findViewById(R.id.msg);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String message = txt.getText().toString();
                Intent i = new Intent("my_filter");
                Bundle bundle = new Bundle();
                bundle.putString("send_data", message);
                i.putExtras(bundle);
                startActivity(i);
            }
        });
    }

}
