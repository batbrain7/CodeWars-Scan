package com.example.mohitkumar.identitiyscan;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AlertDialog;
import android.view.LayoutInflater;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.EditText;
import android.widget.Toast;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    FloatingActionButton f1,f2,f3;
    Animation fabopen, fabclose;
    boolean isopen = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        f1 = (FloatingActionButton) findViewById(R.id.scan);
        f2 = (FloatingActionButton) findViewById(R.id.cam);
        f3 = (FloatingActionButton) findViewById(R.id.text1);
        fabopen = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.fab_open);
        fabclose = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.fab_close);
        f1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isopen) {
                    f2.startAnimation(fabclose);
                    f3.startAnimation(fabclose);
                    f2.setClickable(false);
                    f3.setClickable(false);
                    isopen = false;
                } else {
                    f2.startAnimation(fabopen);
                    f3.startAnimation(fabopen);
                    f2.setClickable(true);
                    f3.setClickable(true);
                    isopen = true;
                }
            }
        });
        final Activity activity = this;
        f2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                IntentIntegrator integrator = new IntentIntegrator(activity);
                integrator.setDesiredBarcodeFormats(IntentIntegrator.ALL_CODE_TYPES);
                integrator.setPrompt("Scan");
                integrator.setCameraId(0);
                integrator.setBeepEnabled(false);
                integrator.setBarcodeImageEnabled(false);
                integrator.initiateScan();
            }
        });

        f3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                AlertDialog.Builder alert = new AlertDialog.Builder(getApplicationContext());
//
//                alert.setTitle("Number");
//                alert.setMessage("Enter the Barcode number");
//
//// Set an EditText view to get user input
//                final EditText input = new EditText(getApplicationContext());
//                alert.setView(input);
//
//                alert.setPositiveButton("Ok", new DialogInterface.OnClickListener() {
//                    public void onClick(DialogInterface dialog, int whichButton) {
//                        Toast.makeText(getApplicationContext(),"Access the server",Toast.LENGTH_SHORT).show();
//                    }
//                });
//
//                alert.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
//                    public void onClick(DialogInterface dialog, int whichButton) {
//                        // Canceled.
//                    }
//                });
//
//                alert.show();
             Intent intent = new Intent(getApplicationContext(),PopUpActivity.class);
                startActivity(intent);
            }
        });
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        IntentResult result = IntentIntegrator.parseActivityResult(requestCode, resultCode, data);
        if (result != null) {
            if (result.getContents() == null) {
                Toast.makeText(this, "Canceled", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(this, "Scanned :" + result.getContents(), Toast.LENGTH_SHORT).show();
                // textView.setText("Scanned    " + result.getContents());
            }
        }
            super.onActivityResult(requestCode, resultCode, data);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_home) {
            // Handle the camera action
        } else if (id == R.id.nav_academic) {

        } else if (id == R.id.nav_library) {

        } else if (id == R.id.nav_personal) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
