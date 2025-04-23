use actix_web::{web, App, HttpServer};
use my_rust_api::routes::user::get_user;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/api/user/{id}", web::get().to(get_user))
    })
        .bind("127.0.0.1:8080")?
        .run()
        .await
}
