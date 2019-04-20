CREATE TABLE `gongyi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(4) DEFAULT NULL COMMENT '1 募捐中 2 执行中 3 已结束',
  `source` char(4) DEFAULT NULL COMMENT '来源 1 ',
  `title` varchar(60) DEFAULT NULL,
  `eOrgName` varchar(45) DEFAULT NULL COMMENT '发起方',
  `pName` text COMMENT '执行方',
  `proj_budget` text,
  `fundName` varchar(45) DEFAULT NULL COMMENT '公募',
  `created_at` datetime DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2048 DEFAULT CHARSET=utf8mb4;
