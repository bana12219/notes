	public void testmember(String member) {
		System.out.println("localmember "+member);// el del metodo- son
		System.out.println("familymember "+this.member);//el de instancia - grandfather
		System.out.println("superlmember "+super.member);//el de superclase- gogfather
		Family f = (familyMember)->{
			System.out.println("local lambda member "+familyMember);// el que se le pasa en lambda-me
			System.out.println("local lambda member (enclosing) "+member);//el que toma del método padre-son
			System.out.println("slocal lambda this member "+this.member);//el de la instancia-grandfather
			System.out.println("slocal lambda super member "+super.member);//el del super padre-gogfather
			return familyMember;
			/*
			 * el scope de la expresion lambda es el mismo que el del método que lo engloba
			 */
		};
		f.who("me");
	}