use std::cmp::Ordering;

pub struct Solution;

impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut minimum = 1;
        let mut maximum = *piles.iter().max().unwrap();
        while minimum < maximum {
            let middle = minimum + (maximum - minimum) / 2;
            let total_hours: i32 = piles.iter().map(|x| Self::eating_time(*x, middle)).sum();
            match total_hours.cmp(&h) {
                Ordering::Greater => minimum = middle + 1,
                _ => maximum = middle,
            }
        }
        minimum
    }

    fn eating_time(pile: i32, k: i32) -> i32 {
        let divisor = pile / k;
        if pile % k == 0 { divisor } else { divisor + 1 }
    }
}
