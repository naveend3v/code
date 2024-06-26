class OOPS_Student {

    public int rollNumber;
    public String studentName;
    public String courseName;
    public int m1,m2,m3;

    public int total(){
        return m1+m2+m3;
    }
    public double average(){
        return (float)total()/3;
    }
    public String grade(){
        if(average()>=70){
            return "A";
        } else if((average()>=60)&&(average()<=69)){
            return "B";
        } else if ((average()>=50)&&(average()<=59)) {
            return "C";
        } else if ((average()>=40)&&(average()<=49)) {
            return "D";
        } else if (average()<40) {
            return "E";
        }
        return "";
    }

    public String details(){
        return "Details : " + "\n"+ "Roll Number : "+ rollNumber + "\n" +  "StudentName : " + studentName + "\n" + "CourseName : " + courseName + "\n" + "Total Marks : " + total() + "\n" + "Average : " + average() + "\n" + "Grade : " + grade() + "\n";
    }

    public static void main(String[] args){
        OOPS_Student s1 = new OOPS_Student();
        s1.rollNumber = 1;
        s1.studentName = "Naveen";
        s1.courseName = "Civil Engineering";
        s1.m1 = 60;
        s1.m2 = 80;
        s1.m3 = 70;

        System.out.println(s1.details());

        OOPS_Student s2 = new OOPS_Student();
        s2.rollNumber = 2;
        s2.studentName = "Ravi";
        s2.courseName = "Mechanical Engineering";
        s2.m1 = 50;
        s2.m2 = 40;
        s2.m3 = 70;

        System.out.println(s2.details());

    }
}
