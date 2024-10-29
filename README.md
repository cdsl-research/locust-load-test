# locust-load-test

### 起動手順

1. テストシナリオ用のConfigMapを作成(自分好みに仕上げる)

2. ConfigMapの適応
   
```
$ kubectl apply -f locustfile-conf.yaml -n locust
```


3. valuesファイルの編集
   
以下のコメントの箇所を変更
```
loadtest:
  # loadtest.name -- a name used for resources and settings in this load test
  name: example
  # loadtest.locust_locustfile -- the name of the locustfile
  locust_locustfile: locustfile.py #locustのファイル名
  # loadtest.locust_locustfile_path -- the path of the locustfile (without trailing backslash)
  locust_locustfile_path: "/mnt/locust" #locustファイルを入れるディレクトリを入れる
  # loadtest.locust_locustfile_configmap -- name of a configmap containing your locustfile (default uses the example locustfile)
  locust_locustfile_configmap: "locustfile" #locustファイルをapplyした後のConfigMapの名前を入れる
  # loadtest.locust_lib_configmap -- name of a configmap containing your lib (default uses the example lib)
```

4. Helmを用いてinstall
```
$ helm install locust deliveryhero/locust -n locust -f values.yaml 
```




もし画像を使うシナリオを行いたいのであれば，以下の手順に従う．

画像をConfigMapにする
```
$ kubectl create configmap locust-image --from-file=image/usecase.png -n locust
```


valuesファイル内の以下の項目をいじる
```
extraConfigMaps:
  locust-image: /mnt/locust/image
```

これで負荷試験できる


