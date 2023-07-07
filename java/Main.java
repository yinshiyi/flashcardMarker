package java;
import javax.swing.*;
 
public class Main 
{
  public static void main(String[] args) 
  {
    //Create a new frame
    JFrame frame = new JFrame("JButton Example");
    //Create button
    JButton btn = new JButton("Click here");
    //Set button position
    btn.setBounds(100,100,100,40);
    //Add button to frame
    frame.add(btn);
    frame.setSize(300,300);
    frame.setLayout(null);
    frame.setVisible(true);  
  }
}
