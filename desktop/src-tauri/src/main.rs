// 윈도우에서 실행할 때 검은 콘솔 창이 같이 뜨지 않게 함
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::Manager;

fn main() {
    tauri::Builder::default()
        // 투어디를 두 번 실행하면 새 창 대신 기존 창을 앞으로 가져옴
        // (창이 두 개면 같은 기록을 동시에 고쳐 "다른 창에서 기록이 바뀌었어요" 충돌이 남)
        .plugin(tauri_plugin_single_instance::init(|app, _args, _cwd| {
            if let Some(w) = app.get_webview_window("main") {
                let _ = w.unminimize();
                let _ = w.show();
                let _ = w.set_focus();
            }
        }))
        // 마지막 창 크기·위치를 기억해 다음 실행 때 그대로 엶
        .plugin(tauri_plugin_window_state::Builder::default().build())
        .run(tauri::generate_context!())
        .expect("투어디를 실행하지 못했어요");
}
