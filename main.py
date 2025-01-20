import logging
import os
from src.utils.config_loader import ConfigLoader
from src.managers.friend_link_manager import FriendLinkManager
# from src.managers.rss_processor import RSSProcessor
# from src.services.notification_service import NotificationService
# from src.services.daily_push_service import DailyPushService

# 日志配置
logging.basicConfig(level=logging.INFO, format="😋 %(levelname)s: %(message)s")

def main():
    # Step 1: 加载配置
    config_path = os.path.join("conf.yaml")
    config = ConfigLoader(config_path)
    
    # Step 2: 初始化管理类和服务类
    friend_manager = FriendLinkManager(config)
    # rss_processor = RSSProcessor(config)
    # notification_service = NotificationService(config)
    # daily_push_service = DailyPushService(config)
    
    # Step 3: 处理友链数据
    spider_settings = config.get_spider_settings()
    if spider_settings['enable']:
        logging.info("开始爬取友链数据...")
        friends = friend_manager.fetch_friend_data()
        # if spider_settings['merge_result']:
        #     result, lost_friends = friend_manager.merge_data(result, lost_friends)
        # friend_manager.save_data_to_files(result, lost_friends)
        # logging.info("友链数据处理完成")
    
    # # Step 4: 处理 RSS 更新
    # if config["rss_subscribe"]["enable"]:
    #     logging.info("开始处理 RSS 更新...")
    #     latest_articles = rss_processor.get_rss_updates()
    #     if latest_articles:
    #         email_list = rss_processor.get_email_list()
    #         if email_list:
    #             rss_processor.send_email_updates(latest_articles, email_list)
    #         else:
    #             logging.info("无订阅用户")
    #     else:
    #         logging.info("无新文章，无需推送")
    
    # # Step 5: 每日推送（如启用）
    # if config.get("daily_push", {}).get("enable"):
    #     logging.info("开始每日推送...")
    #     daily_push_service.push_recommendations()
    
    # logging.info("程序执行完毕")

if __name__ == "__main__":
    main()
