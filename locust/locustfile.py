from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def on_start(self):
        self.client.get("/")  # サーバーに最初にアクセスするための初期化

    @task
    def send_image(self):
        url = "/post/"  # 送信先URLを指定
        # 画像ファイルを開く
        with open('image/usecase.png', 'rb') as image_file:
            files = {
                'file-246': ('usecase.png', image_file, 'image/png')  # 画像をfile-246に設定
            }
            # フォームデータを設定
            data = {
                '_wpcf7': '13',
                '_wpcf7_version': '5.9.8',
                '_wpcf7_locale': 'ja',
                '_wpcf7_unit_tag': 'wpcf7-f13-p9-o1',
                '_wpcf7_container_post': '9',
                '_wpcf7_posted_data_hash': '',  # ハッシュを空にする
                'your-name': 'mana',
                'your-email': 'c0a201310c@edu.teu.ac.jp',
                'your-subject': '予約について',
                'your-message': 'ajdjadjcsdjv'
            }
            # POSTリクエストでデータを送信
            self.client.post(url, files=files, data=data)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # 1〜5秒の間でリクエストの待機時間を設定

