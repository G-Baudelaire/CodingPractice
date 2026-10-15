use std::iter::zip;

pub struct Solution;

impl Solution {
    pub fn is_anagram_sorting(s: String, t: String) -> bool {
        let mut s_chars: Vec<char> = s.chars().collect();
        let mut t_chars: Vec<char> = t.chars().collect();
        s_chars.sort();
        t_chars.sort();
        s_chars == t_chars
    }
}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut counts: Vec<i16> = vec![0; 26];
        let origin = 'a' as usize;

        for (char_s, char_t) in zip(s.chars(), t.chars()) {
            counts[char_s as usize - origin] += 1;
            counts[char_t as usize - origin] -= 1;
        }

        counts.iter().all(|&v| v == 0)
    }
}
