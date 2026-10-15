pub struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut left = 0;
        let mut longest_substring = 0;
        let mut char_counts = vec![0; 256];
        let characters: Vec<char> = s.chars().collect();

        for right in 0..characters.len() {
            let right_character: usize = characters[right] as usize;
            char_counts[right_character] += 1;

            if Self::is_unique(&char_counts) {
                longest_substring += 1;
            } else {
                let left_character: usize = characters[left] as usize;
                char_counts[left_character] -= 1;
                left += 1;
            }
        }

        longest_substring
    }

    fn is_unique(v: &[i32]) -> bool {
        v.iter().all(|&x| x <= 1)
    }
}
