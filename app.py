from yt_dlp import YoutubeDL

def download_youtube_video(url):
    # 配置下载选项
    ydl_opts = {
        'format': 'best',  # 下载最佳质量
        'outtmpl': '%(title)s.%(ext)s',  # 输出文件模板
    }
    
    # 创建下载器实例
    with YoutubeDL(ydl_opts) as ydl:
        try:
            # 下载视频
            ydl.download([url])
            print("下载完成!")
        except Exception as e:
            print(f"下载出错: {str(e)}")

def download_bili_video(url):
    # 配置下载选项
    ydl_opts = {
        'format': 'bv*[height<=1080]+ba/b',  # Bilibili视频格式，1080P及以下
        'outtmpl': '%(title)s.%(ext)s',  # 输出文件模板
        # Bilibili 特定设置
        'cookiesfrombrowser': ('firefox',),  # 从 Firefox 浏览器获取 cookies
        'concurrent_fragment_downloads': 8,  # 并发下载片段数
        'extractor_retries': 3,  # 重试次数
    }
    
    # 创建下载器实例
    with YoutubeDL(ydl_opts) as ydl:
        try:
            # 获取视频信息和可用格式
            info = ydl.extract_info(url, download=False)
            print("\n可用的格式：")
            for f in info['formats']:
                print(f"格式ID: {f.get('format_id', 'N/A')}, "
                      f"分辨率: {f.get('resolution', 'N/A')}, "
                      f"文件格式: {f.get('ext', 'N/A')}")
            
            # 下载视频
            ydl.download([url])
            print("下载完成!")
        except Exception as e:
            print(f"下载出错: {str(e)}")

if __name__ == "__main__":
    # 输入要下载的视频URL
    # https://www.youtube.com/watch?v=k4715CJ0Ii8

    download_bili_video("https://www.bilibili.com/video/BV1gaByY5EH4/?spm_id_from=333.1073.high_energy.content.click")