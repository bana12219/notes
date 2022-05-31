package com.example.java.algsdatastru;

public class performance {
/*
 * performance es que tantos recursos consume tu codigo
 * mejorar el codigo no significa mejorar el consumo
 * tiempo cuanto tarda, numero de operaciones y complejidad
 * spacio memoria, almacenamiento
 * network cuanto transfiere, ancho de banda e informacion transferida entre maquinas
 * encontrar balance entre estas implica por ejemplo que tantos datos guardas en memoria 
 * en vez de hacer operaciones
 * complejidad es que tanto cambian tus requisitos cuando el problema crece
 * depende del tamaño del input
 * que tanto cambia el performance si son muchos datos
 * 
 * 
 * TIEMPO depende de cuantas operaciones básicas haces
 * 		aritmeticas
 * 		lectura y escritura
 * 		asignacion
 * 		test (a==b)
 * 	todas las operaciones complejas se pueden descomponer en operaciones básicas
 *  pensar la manera en que el numero se multiplica con el numero de inputs
 *  piensa en el peor caso, cual es el maximo numero de operaciones que se van a ejecutar en
 *  el peor caso
 * se trata de evaluar no cuantas operaciones haces en uno, 
 * si no como se multiplican cuando son 2000
 */
/*
 * Big o notation
 *  o(1) un algorithmo que no incrementa así sea 10, o 10000, su complejidad es constante 
 *  		si tarda 10 seg, tarda 10 seg 
 *  n es el size del input
 *  	o(n) el algoritmo incrementa con el input, si son 200 tarda 200 mins
 *  o(n^2) el algoritmo tarda el cuadrado del input
 *  	puede ser 
 *  		o(n^2 +100) o o(n^2 +n) no importa va a ser o(n^2)
 *  
 */
	
/*o(1)
 * la complejidad va a radicar en el tamaño del input, el
 * tiempo constante de operacion no es afectado por el tamaño del input, 
 */
public static void tiempoConstante(int n) {
	int a=3,b=4;
	int suma=a+b+n;
	int producto=a*b*n;
	System.out.println(suma+"  "+producto);
}
/*o(n)
 * el tamaño de n es del input 
 * la complejidad  es de orden de n, si n incrementa incrementa tambien el numero de op
 * incrementa linear
 */
public static void linear(int n) {
	for (int i=0; i<n;++i) {
		System.out.println(i);
	}
}
/*o(n^2)
 * loops anidados
 */
	public static void cuadratic(int n) {
		for (int i=0; i<n;++i) {
			for (int x=0; i<n;++i) {
				System.out.println(i);
			}
		}
	}
/*o(n+100)
 * asumamos que n es muy largo el tiempo estrá determinado por el tamaño de n
 * mas 100 del otro loop
 */
		public static void linearconstate(int n) {
			for (int i=0; i<n;++i) {
					System.out.println(i);
			}
			for (int i=0; i<100;++i) {
				System.out.println(i);
			}
	
}
/*
 * o(n+m)
 * inputs independeintes, 
 */
public static void npm(int n,int m) {
			for (int i=0; i<n;++i) {
					System.out.println(i);
			}
			for (int i=0; i<m;++i) {
				System.out.println(i);
			}
	
}
/*
 * o(n*m)
 * inputs independeintes, pero bucles anidados
 */
public static void nmm(int n,int m) {
			for (int i=0; i<n;++i) {
					System.out.println(i);

					for (int s=0; s<m;++s) {
						System.out.println(s);
					}
	}
	
}
/*o(n^2)
 * loops anidados mas otro loop, como solo dependemos de n 
 * el resto se desprecia
 */
public static void cuadr(int n) {
		for (int i=0; i<n;++i) {
			for (int x=0; i<n;++i) {
				System.out.println(i);
			}
		}
		for (int s=0; s<n;++s) {
			System.out.println(s);
		}
	}

	
	
	
	
	
	
	
	
}
