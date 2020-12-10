import java.io.File;
import java.util.*;

public class Main {
    public static ArrayList<ArrayList<String>> inputPart1() {
        File readFile = new File("/Users/max/Desktop/Tutorials/AdventOfCode/Day7/src/input.txt");
        ArrayList<ArrayList<String>> colors = new ArrayList<>();
        try {
            Scanner fileReader = new Scanner(readFile);

            // READ FILE
            while (fileReader.hasNextLine()) {
                String data = fileReader.nextLine();

                if(!data.contains("contain no other bags")) {
                    String[] arrOfStr = data.split(" ");
                    ArrayList<String> colorsOnLine = new ArrayList<>();
                    String[] wordsToRemove = {"bags", "contain", "bags,", "bag,", "bags.", "bag."};
                    List<String> notToAdd = Arrays.asList(wordsToRemove);
                    String colorToAdd = "";

                    for (int i = 0; i < arrOfStr.length; ++i) {
                        if (i % 4 == 0) { colorToAdd = ""; }
                        if (!notToAdd.contains(arrOfStr[i]) && !strIsInt(arrOfStr[i])) { colorToAdd += arrOfStr[i]; }
                        if ((i + 1) % 4 == 0) { colorsOnLine.add(colorToAdd); }
                    }
                    colors.add(colorsOnLine);
                }
            }
            return colors;
        } catch (Exception E) {
            System.out.println("BRA? BRA?");
            System.out.println(E);
        }
        return new ArrayList<>();
    }



    public static void part1() {
        ArrayList<ArrayList<String>> colors = inputPart1();
        Set<String> correctBags = new HashSet<>();
        correctBags.add("shinygold");

        int behindCounter = 0;
        int bagCounter = correctBags.size();

        while(behindCounter < bagCounter) {
            behindCounter = bagCounter;
            ArrayList <String> bagsToAdd = new ArrayList<>();
            for (ArrayList<String> color : colors) {
                for (int j = 0; j < color.size(); ++j) {
                    if (correctBags.contains(color.get(j))) {
                        if (j - 1 >= 0) {
                            bagsToAdd.add(color.get(0));
                            break;
                        }
                    }
                }
            }
            correctBags.addAll(bagsToAdd);
            bagCounter = correctBags.size();
        }
        System.out.println("Result part 1 = " + (correctBags.size() - 1));
        System.out.println("BRA BRA");
    }


    public static void part2() {
        File readFile = new File("/Users/max/Desktop/Tutorials/AdventOfCode/Day7/src/input.txt");
        ArrayList<HashMap<String, Integer>> colors = new ArrayList<>();
        ArrayList<String> startingColors = new ArrayList<>();
        try {
            Scanner fileReader = new Scanner(readFile);

            // READ FILE
            while (fileReader.hasNextLine()) {
                String data = fileReader.nextLine();

                String[] splitArr = data.split(" ");
                String startingColorToAdd = splitArr[0] + splitArr[1];
                startingColors.add(startingColorToAdd);

                if(!data.contains("contain no other bags")) {
                    String[] arrOfStr = data.split(" ");
                    HashMap<String, Integer> bagsOnLine = new HashMap<String, Integer>();
                    String[] wordsToRemove = {"bags", "contain", "bags,", "bag,", "bags.", "bag."};
                    List<String> notToAdd = Arrays.asList(wordsToRemove);
                    String colorToAdd = "";
                    int numberToAdd = 0;

                    for (int i = 0; i < arrOfStr.length; ++i) {
                        if (i % 4 == 0) {
                            colorToAdd = "";
                            numberToAdd = 0;
                        }
                        if (!notToAdd.contains(arrOfStr[i]) && !strIsInt(arrOfStr[i])) {
                            colorToAdd += arrOfStr[i];
                            if(i - 1 >= 0) {
                                if (strIsInt(arrOfStr[i - 1])) {
                                    numberToAdd = Integer.parseInt(arrOfStr[i - 1]);
                                }
                            } else {
                                numberToAdd = 1;
                            }
                        }
                        if ((i + 1) % 4 == 0) {
                            bagsOnLine.put(colorToAdd, numberToAdd);
                        }
                    }
                    colors.add(bagsOnLine);
                } else {
                    String[] arrOfStr = data.split(" ");
                    String colorToAdd = arrOfStr[0] + arrOfStr[1];
                    HashMap<String, Integer> bagsOnLine = new HashMap<String, Integer>();
                    bagsOnLine.put(colorToAdd, 1);
                    colors.add(bagsOnLine);
                }
            }
            fileReader.close();

            //Solution
            Set<String> correctBags = new HashSet<>();
            correctBags.add("shinygold");
            HashMap<String, Integer> bagsValue = new HashMap<>();
            bagsValue.put("shinygold", 1);
            int behindCounter = 0;
            int bagCounter = correctBags.size();

            int result = 0;

            while(behindCounter < bagCounter) {
                behindCounter = bagCounter;
                ArrayList <String> bagsToAdd = new ArrayList<>();
                ArrayList <Integer> numbersToAdd = new ArrayList<>();

                for(int i = 0; i < startingColors.size(); ++i) {
                    ArrayList<String> colorsToCheck = new ArrayList<>(bagsValue.keySet());
                    if(colorsToCheck.contains(startingColors.get(i))) {
                        //TODO might be wrong approach, check later
                        int multiplicator = bagsValue.get(startingColors.get(i));
//                        System.out.println("multiplicator = " + multiplicator);
                        for(String key : colors.get(i).keySet()) {
                            // System.out.println("matching color: " + key);
                            if(!startingColors.get(i).equals(key)) {
                                if (!colorsToCheck.contains(key)) {
//                                    System.out.println("multiplicator = " + multiplicator);
                                    int numberForResult = colors.get(i).get(key);
                                    result += numberForResult * multiplicator;
//                                    result += numberForResult;
//                                    System.out.println("ADDED = " + key + " " + (numberForResult * multiplicator));
                                    numbersToAdd.add(numberForResult * multiplicator);
                                    bagsToAdd.add(key);
                                }
                            }
                            // System.out.println( key );
                            // System.out.println( colors.get(i).get(key) );
                        }
                    }
                }
//                bagsValue = new HashMap<>();
                System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
                ArrayList<String> existingBags = new ArrayList<>(bagsValue.keySet());
                for(int i = 0; i < bagsToAdd.size(); ++i) { //TODO is value in bags
                    if (!existingBags.contains(bagsToAdd.get(i))) {
                        System.out.println(bagsToAdd.get(i) + "\t" + numbersToAdd.get(i));
                        bagsValue.put(bagsToAdd.get(i), numbersToAdd.get(i));
                    }
                }
                System.out.println("Current result = " + result);
                correctBags.addAll(bagsToAdd);
                bagCounter = bagsValue.size();
            }

            // 1319 too low
            System.out.println("Result part 2 = " + result);


            System.out.println("BRA BRA");
        } catch (Exception E) {
            System.out.println("BRA? BRA?");
            System.out.println(E);
        }
    }


    private static boolean strIsInt(String s) {
        try {
            int isNum = Integer.parseInt(s);
        } catch (NumberFormatException nfe) {
            return false;
        }
        return true;
    }


    public static void main(String[] args) {
        //part1();
        part2();
    }
}
