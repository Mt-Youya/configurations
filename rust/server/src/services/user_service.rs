use crate::models::user::User;

pub async fn get_user_service(user_id: u32) -> Option<User> {
    if user_id == 1 {
        Some(User {
            id: user_id,
            name: "John Doe".to_string(),
            email: "john@example.com".to_string(),
        })
    } else {
        None
    }
}
