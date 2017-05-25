import java.io.*;
import java.net.*;
import java.util.*;
public class UDPTimeServer{
	public static void main(String args[]) throws IOException{
		DatagramSocket serverSocket=new DatagramSocket(9876);
		byte[] sendData=new byte[1024];
		byte[] receiveData=new byte[1024];
		while(true){
			DatagramPacket receivePacket=new DatagramPacket(receiveData,receiveData.length);
			serverSocket.receive(receivePacket);
			//DateFormat dateFormat=new DateFormat("yyyy-MM-dd HH:mm:ss");
			Date curr=new Date();
			String currDate=curr.toString();
			if(Integer.parseInt(currDate.substring(11,13))>=12)
				currDate=currDate+" Good Evening ";
			else
				currDate=currDate+" Good Morning ";
			InetAddress IPAddress=receivePacket.getAddress();
			int port=receivePacket.getPort();
			sendData=currDate.getBytes();
			DatagramPacket sendPacket=new DatagramPacket(sendData,sendData.length,IPAddress,port);
			serverSocket.send(sendPacket);
		}
	}
}