import java.io.*;
import java.net.*;
public class server {
public static void main(String[] args){
try{
	ServerSocket ss =new ServerSocket(6666);
	Socket s =ss.accept();
	DataInputStream dis =new DataInputStream(s.getInputStream());
	DataOutputStream dout= new DataOutputStream(s.getOutputStream());
	String str="";
	while(str.indexOf("exit")== -1 ){
		str =(String)dis.readUTF();
		StringBuilder str1= new StringBuilder(str);
		str1.reverse();
		str=String.valueOf(str1);
		dout.writeUTF(str.toUpperCase());
		dout.flush();
	}
	ss.close();
    }catch(Exception e){
	System.out.println(e);}
}
}