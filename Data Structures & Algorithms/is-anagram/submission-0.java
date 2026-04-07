class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        List<Character> ss = new ArrayList<>();
        List<Character> tt = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            ss.add(s.charAt(i));
        }
        for (int j = 0; j < t.length(); j++) {
            tt.add(t.charAt(j));
        }
        Collections.sort(ss);
        Collections.sort(tt);

        return (ss.equals(tt));
    }
}
