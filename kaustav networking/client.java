import java.io.*;
import java.net.*;
public class client{
	public static void main(String[] args) throws IOException{
		try{
			BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
			Socket s =new Socket("localhost",6666);
			DataInputStream dis =new DataInputStream(s.getInputStream());
			DataOutputStream dout= new DataOutputStream(s.getOutputStream());
			String str="";
			while(!str.equals("exit")){
			str= br.readLine();
			dout.writeUTF(str);
			dout.flush();
			String str1 =(String)dis.readUTF();
			System.out.println("SERVER ECHO: "+str1);
			}
			dout.close();
			s.close();
			
		}catch(Exception e){ System.out.println(e);}
	}
}