package com.agabasoft.levis.app;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class ResultsActivity extends AppCompatActivity {
//    public final static String mulyrica_secret = "x3IkD8_BT5es_TO7N0xtd2Nmcy2lT25RYlK4x5lEXfXwfPPPnyk1Rq6m_GxHVA5S29H8iIq3zWtBYbiXZNKZ5A";
//    public final static String mulyrica_access_token = "t6QbS_YALOsj7TYV5864GiaxDu8l6norvbVpQBk7rjTAhZXm5VNZhNHPLpBogpAQ";
    public String[] input_fields;
    public String song_artist="";

    @Override
    protected void onCreate(Bundle savedInstanceState) throws NullPointerException{
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_results);

        if (getIntent() != null && getIntent().hasExtra(Intent.EXTRA_TEXT)) {
            //Make a request and populate the
            Bundle extras = getIntent().getExtras();
            input_fields = extras.getStringArray(getIntent().EXTRA_TEXT);
            if(input_fields == null) throw new NullPointerException();
            TextView lyrics = findViewById(R.id.lyrics);
            song_artist = input_fields[0]+input_fields[1];
            lyrics.setText(song_artist);
        }
    }


}
