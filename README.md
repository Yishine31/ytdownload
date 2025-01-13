# ytdownloadg 使用說明
### Youtube影片/音檔下載程式

- yt_download_audio 用於下載 Youtube影片的音檔(mp3)
    - 如果批量下載的音檔中有出現錯誤，他會自動跳過該檔案並執行後續下載。
    - 使用時需要手動輸入檔案總數(total)，與欲下載的播放清單網址(url)，
    pathdir 可以修改檔案下載的位址。
- yt_download_mp4 用於下載 Youtube影片檔(mp4)
    - 使用時需要手動輸入欲下載的播放清單網址(url)，pathdir 可以修改檔案下載的位址。
    - 下載影片共有3種模式選擇:
        1. download_lowest_lsit 用於以最低畫質批量下載整個播放清單。
        2. download_single 用於以最高畫質下載單支影片。
        3. download_lowest_single 用於以最低畫質下載單支影片。
