use actix_web::{web, HttpResponse};
use my_rust_api::services::user_service::get_user_service;
use my_rust_api::models::user::User;

pub async fn get_user(path: web::Path<(u32,)>) -> HttpResponse {
    let user_id = path.into_inner().0;
    match get_user_service(user_id).await {
        Some(user) => HttpResponse::Ok().json(user),
        None => HttpResponse::NotFound().finish(),
    }
}
