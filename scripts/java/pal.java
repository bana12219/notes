import java.time.Instant;

import java.util.stream.Stream;

import java.time.LocalDateTime;
import java.time.Period;
import java.time.temporal.Temporal;
import java.time.Duration;

//Instant start = Instant.now();
void funct(){
LocalDateTime start= LocalDateTime.now();
LocalDateTime stop;
String word="Never Odd or Even".replaceAll("\\s", "").toLowerCase();
Boolean b=(new StringBuilder(word).reverse().toString()).equals(word);
stop= LocalDateTime.now();
System.out.println(Duration.between(start, stop)+" - "+b);
}

void funct2(){
    LocalDateTime start= LocalDateTime.now();
	LocalDateTime stop;
	String word="Never Odd or Even";
	String derecho="", reves="";
	for (String s : Arrays.asList(word) ){
		if (!s.isBlank()) {
			derecho+=s;
			reves=s+reves;
		}
	}
	Boolean b=derecho.equals(reves);
	stop= LocalDateTime.now();
	System.out.println(Duration.between(start, stop)+" - "+b); 
}


class Estatics{
	static Integer i=5;
	public Integer i2=10;
}


Estatics e1= new Estatics ();
Estatics e2=new Estatics();
 e1= new Estatics ();
 e2=new Estatics();
System.out.println("Variables estaticas pueden ser publicas o no\n"+ Estatics.i
+"\n"+e2.i
+"\n"+e1.i
+"\n"+e2.i2
+"\n"+e1.i2

);

Estatics.i=0;
e2.i2=3;
System.out.println("Variables estaticas pueden ser publicas o no\n"+ Estatics.i
+"\n"+e2.i
+"\n"+e1.i
+"\n"+e2.i2
+"\n"+e1.i2

);