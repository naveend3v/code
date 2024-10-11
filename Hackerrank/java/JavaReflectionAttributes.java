// https://www.hackerrank.com/challenges/java-reflection-attributes/problem
// Java Reflections
// https://docs.oracle.com/javase/tutorial/reflect/class/classMembers.html

import java.lang.reflect.*;
import java.util.*;

class Student1 {
    private String name;
    private String id;
    private String email;

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}

class JavaReflectionAttributes {

    public static void main(String[] args) {
        Class student1 = new Student1().getClass();
        Method[] methods = student1.getDeclaredMethods();

        ArrayList<String> methodList = new ArrayList<>();
        for (Method m : methods){
            methodList.add(m.getName());
        }
        Collections.sort(methodList);
        for (String name : methodList) {
            System.out.println(name);
        }
    }

}



