package com.agabasoft.levis.app;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    final EditText song = (EditText) findViewById(R.id.song);
    final EditText artist = (EditText) findViewById(R.id.artist);
    public String input_song, input_artist;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
/*
        Button go = findViewById(R.id.analyze);
        go.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(incompleteForm())
                    Toast.makeText(view.getContext(), "All fields are required.",
                            Toast.LENGTH_SHORT).show();
                else launchIntent(view);
            }
        });*/
    }

    /** Launch lyrics/results activity
     * Should be called after calling incompleteForm
     * */
    public void launchIntent(View view) {
        Intent resultsIntent = new Intent(this, ResultsActivity.class);
        String[] input_array = {song.getText().toString(), artist.getText().toString()};
        resultsIntent.putExtra(Intent.EXTRA_TEXT, input_array);
        startActivity(resultsIntent);
    }

    public boolean incompleteForm() {
        input_song = song.getText().toString();
        input_artist = artist.getText().toString();
        return (input_song.matches("") || input_artist.matches("") );
    }
}
