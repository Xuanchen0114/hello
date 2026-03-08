# hello

使用 FastAPI 建立的最小 Hello World 網頁伺服器。

## 本機執行方式

1. 安裝套件：

```bash
pip install -r requirements.txt
```

2. 啟動伺服器：

```bash
uvicorn main:app --reload
```

3. 開啟瀏覽器到 `http://127.0.0.1:8000`，會看到 `Hello World`。

## 在 GitHub Actions 上預覽

此專案新增了 **Review web server** workflow（`.github/workflows/review-web-server.yml`），可在 GitHub 上啟動伺服器並產生可下載的預覽檔案。

### 觸發方式

- 手動：到 GitHub 的 **Actions** 頁面執行 `Review web server`（`workflow_dispatch`）。
- 自動：對 `main` 的 push 與 pull request 也會執行。

### 查看結果

Workflow 會：

1. 安裝 `requirements.txt` 內的依賴
2. 啟動 FastAPI 伺服器
3. 抓取首頁內容到 `page.html`
4. 上傳 `page.html` 與 `server.log` 為 artifact：`web-server-review`

下載 artifact 後，直接打開 `page.html` 就能檢視頁面內容。
