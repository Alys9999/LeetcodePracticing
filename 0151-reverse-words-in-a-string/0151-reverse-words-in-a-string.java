class Solution {
    public String reverseWords(String s) {

        Stack<String> st = new Stack<>();
        StringBuilder sb = new StringBuilder();
        char[] charArray = s.toCharArray();

        for (int i = 0; i < charArray.length; i++) {
            if (charArray[i] == ' ') {
                st.push(sb.toString());
                sb.setLength(0);
            } else if (i == charArray.length - 1) {
                sb.append(charArray[i]);
                st.push(sb.toString());
            } else {
                sb.append(charArray[i]);
            }
        }

        StringBuilder res = new StringBuilder();
        while (!st.isEmpty()) {
            String cur = st.pop();
            res.append(cur);
            if (!cur.equals("")) {
                res.append(" ");

            }

        }
        return res.toString().trim();
    }
}