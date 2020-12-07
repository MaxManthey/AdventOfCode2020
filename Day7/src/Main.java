import java.io.File;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        File readFile = new File("/Users/max/Desktop/Tutorials/AdventOfCode/Day7/src/input.txt");
        try {
            Scanner fileReader = new Scanner(readFile);
            ArrayList<ArrayList<String>> colors = new ArrayList<>();

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
}
