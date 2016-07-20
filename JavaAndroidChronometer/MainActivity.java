package com.hivemind.zerodavila.chronometerexample;

import android.content.DialogInterface;
import android.os.SystemClock;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Chronometer;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button startChrono;
    Button pauseChrono;
    Chronometer chrono;
    long time = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        startChrono = (Button) findViewById(R.id.startBtn);
        pauseChrono = (Button) findViewById(R.id.pauseBtn);
        chrono = (Chronometer) findViewById(R.id.chron);
        startChrono.setOnClickListener(this);
        pauseChrono.setOnClickListener(this);
    }

    @Override
    public void onClick(View arg0) {
        switch (arg0.getId()) {

            case R.id.startBtn:
                chrono.setBase(SystemClock.elapsedRealtime() + time);
                chrono.start();
                break;

            case R.id.pauseBtn:
                time = chrono.getBase() - SystemClock.elapsedRealtime();
                chrono.stop();
                break;

        }
    }
}
