import java.io.*;
import java.net.*;
import java.util.Date;
public class serverd {
public static void main(String[] args){
try{
	ServerSocket ss =new ServerSocket(6666);
	Socket s =ss.accept();
	DataInputStream dis =new DataInputStream(s.getInputStream());
	DataOutputStream dout= new DataOutputStream(s.getOutputStream());
	String str="";
	while(str.indexOf("exit")== -1 ){
		str =(String)dis.readUTF();
		if(str.equals("datetime"))
		{
			Date date = new Date();
			str=date.toString();
			if(Integer.parseInt(str.substring(11,13))>=12)
			{
				str=str+" Good Evening";
			}
			else
			{
				str=str+" Good Morning";
			}
		}
		dout.writeUTF(str);
		dout.flush();
	}
	ss.close();
    }catch(Exception e){
	System.out.println(e);}
}
}