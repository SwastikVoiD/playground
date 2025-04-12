import java.io.*;
public class input {
    public static void main(String args[]){
        double x, y, z;
        x = 12;
        y = 12;
        z = x/y;
        System.out.println(z);
        try{
            FileOutputStream ioObj = new FileOutputStream("C:\\Users\\swast\\Desktop\\GITHUB\\playground\\Java\\PRACTICE\\FIle Handeling\\input.txt");
            ioObj.write(null);;
            ioObj.close();
        } catch(Exception e){
            String a = e.getMessage();
            System.out.println(a);
            return;
        }

        

    }

}
