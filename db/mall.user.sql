-- 玩个干净点的数据库,删除数据库
DROP  mall;

-- 创建想要的数据库
CREATE database mall;


use mall;
--建表
CREATE TABLE tb_user (
	`id` int(11) NOT NULL auto_increment,
	`username` varchar(20) NOT NULL,
	`password` varchar(50) NOT NULL,
	`email` varchar(30) NOT NULL,
	`phone` varchar(11) NOT NULL,
	`address` varchar(50),
	PRIMARY KEY (`id`),
	UNIQUE KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO tb_user (username,password,email,phone,address) VALUES ('newxieyang','da927a5c6e83e085ead9305bbe64c2e9','newxieyang@msn.cn','tianyuan.12','hen');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('hdfgh','2cc953a30556effcf705c6dfa53c2cfe','gdghgfhf','ghfgh','fghdfghdfghdf');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('jfjghjf','87e3128b483abb3500a1e9ea56aa2bea','jghj','ghjfhjfg','jfjgfhtuy');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('kghkghj','6b174ab4ad8d4b783e4bd9a7cd443552','ghjkghjk','kghjk','ghjkghjkghj');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('vzxvsf','49c153c2b1dee2c29b6eaf4457f1c9f2','easdf','asdf','asdfasdfasd');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('kiss','9067d941c771d2c73ffc5a48be5670d9','foxmail','fjkdkf','hengdong');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('cullen','kissyou','newxieyang@msn.cn','18621618053','hengdong');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('han','7e8dc9bbd86d1f1ff179f09f36b50c6d',' nerver','13397478793','kind');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('谢洋洋','142084157beb09e5cd08c85629319e1c','kkk','dfd','fdsfdsf');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('溜冰','44f21d5190b5a6df8089f54799628d7e','fkdsf','付款撒发','kj');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('他','be1729596fa13efb892973818f20735d','发送打法速度发送的','15096011434','发达发送打法速度');
INSERT INTO tb_user (username,password,email,phone,address) VALUES ('旺盛','40654cf30cf8c58c62f338fdfbc51830','jkfdkjfds','kfkjsd','kjkfjdk');
