#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(self: &Self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Self) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let rect = Rectangle {
        width: 30,
        height: 50
    };

    let small_rect = Rectangle {
        width: 20,
        height: 40
    };

    let big_rect = Rectangle {
        width: 40,
        height: 70
    };

    println!(
        "The area of the rectangle {:?} is {} square pixels.",
        rect,
        rect.area()
    );

    println!("Can rect hold the small? {}", rect.can_hold(&small_rect));
    println!("Can rect hold the big? {}", rect.can_hold(&big_rect));
}
