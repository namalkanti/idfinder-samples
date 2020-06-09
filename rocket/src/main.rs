#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

use std::fs;
use rocket::response::content;
use serde_json::Value;

#[get("/")]
fn index() -> content::Json<String> {
    let json = fs::read_to_string("data.json")
        .expect("Couldn't open file.");
    content::Json(json)
}

#[get("/<id>")]
fn detail(id: u8) -> content::Json<String> {
    let json_string = fs::read_to_string("data.json")
        .expect("Couldn't open file.");
    let json: Value = serde_json::from_str(&json_string).unwrap();
    let pk = id.to_string();
    let card = &json[pk];
    content::Json(card.to_string())
}

fn main() {
    rocket::ignite().mount("/", routes![index, detail]).launch();
}
