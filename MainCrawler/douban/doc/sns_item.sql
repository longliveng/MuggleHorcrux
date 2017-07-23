CREATE TABLE `sns_item` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `content` text COMMENT '内容',
  `url` varchar(255) NOT NULL COMMENT 'item的链接',
  `item_date` datetime NOT NULL COMMENT 'item创建时间',
  `platform` tinyint(2) NOT NULL COMMENT '内容来源. 1:豆瓣 2:微博',
  `account` varchar(45) DEFAULT NULL COMMENT '账号名称，名称必须是唯一标识用户的，可以用数字id',
  `img_url` text COMMENT '图片原始url,带域名',
  `img_path` text COMMENT '储存图片到本地的相对路径',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='爬sns 的feed';
