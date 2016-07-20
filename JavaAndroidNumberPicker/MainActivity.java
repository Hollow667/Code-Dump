package com.hivemind.zerodavila.numberpickerexample;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.NumberPicker;

public class MainActivity extends AppCompatActivity {

    //Declare Variables
    NumberPicker noPicker = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Numeber picker 1
        noPicker = (NumberPicker) findViewById(R.id.pickNumber1);
        noPicker.setMaxValue(1000);
        noPicker.setMinValue(0);
        noPicker.setWrapSelectorWheel(false);

    }
}
