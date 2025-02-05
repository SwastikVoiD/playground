public class type_conversion {
    public static void main(String[] args) {
        // Type Conversion and type casting
        //  we cannot change the type of a variable ;
        //  we can assign different type values to different vars under some constraints
        byte b = 127;
        int a = 12;
        // b = a; this doesnt work
        // a = b; works cuz this is implicit conversion
        b = (byte) a; // this works and is known as explicit converion or casting
        System.out.println(b);
        // casting or explicit conversion
        
        float f = 5.6f;
        int x = (int) f;
        System.out.println(x);

        // explicit csting when going out of range
        byte c = 127;
        int d = c;
        System.out.println(d);

        byte k = (byte) d;
        System.out.println(k);
        
        
        /* we can convert numbers with lower ranges to higher ranges implicitly
         * but to convert numbers with higher ranges into lower ones 
         * we need to do explicit conversion while we neeed to specify the type to both variables in a statement
         * 
         * 
         * 
         */
    }
}
