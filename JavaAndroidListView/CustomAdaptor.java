package com.hivemind.zerodavila.listview2;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class CustomAdaptor extends ArrayAdapter {

    CustomAdaptor(Context context, String[] foods) {
        super(context, R.layout.custom_row, foods);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater myInflater = LayoutInflater.from(getContext());
        View customView = myInflater.inflate(R.layout.custom_row, parent, false);

        String singleFoodItem = String.valueOf(getItem(position));
        TextView myText = (TextView) customView.findViewById(R.id.myText);
        ImageView myImage = (ImageView) customView.findViewById(R.id.myImage);

        myText.setText(singleFoodItem);
        myImage.setImageResource(R.drawable.image);
        return customView;
    }
}
