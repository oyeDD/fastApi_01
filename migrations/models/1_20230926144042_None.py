from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `sys_user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `username` VARCHAR(20) NOT NULL UNIQUE COMMENT '账号',
    `password` VARCHAR(20) NOT NULL  COMMENT '密码',
    `nickname` VARCHAR(20) NOT NULL  COMMENT '昵称',
    `email` VARCHAR(255) NOT NULL  COMMENT '邮箱',
    `created_at` DATETIME(6) NOT NULL,
    KEY `idx_sys_user_usernam_29caba` (`username`),
    KEY `idx_sys_user_nicknam_f5cda9` (`nickname`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `user_Order` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `order_number` VARCHAR(20) NOT NULL,
    `total_amount` DECIMAL(10,2) NOT NULL,
    `order_date` DATETIME(6) NOT NULL,
    `user_id_id` INT NOT NULL,
    CONSTRAINT `fk_user_Ord_sys_user_402f9af7` FOREIGN KEY (`user_id_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `user_Profile` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `avatar` VARCHAR(255) NOT NULL  COMMENT '头像',
    `address` VARCHAR(255) NOT NULL  COMMENT '地址',
    `phone` VARCHAR(20) NOT NULL  COMMENT '电话号码',
    `user_id_id` INT NOT NULL,
    CONSTRAINT `fk_user_Pro_sys_user_d21898ac` FOREIGN KEY (`user_id_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `sys_Settings` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `theme` VARCHAR(255) NOT NULL  COMMENT '主题',
    `notifications` BOOL NOT NULL,
    `language` VARCHAR(50) NOT NULL,
    `user_id_id` INT NOT NULL,
    CONSTRAINT `fk_sys_Sett_sys_user_b2dc2966` FOREIGN KEY (`user_id_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `sys_role` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `role_name` VARCHAR(10) NOT NULL  COMMENT '角色名称',
    `desc` VARCHAR(60)   COMMENT '描述',
    KEY `idx_sys_role_role_na_e4636f` (`role_name`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `sys_user_role` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `role_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_sys_user_sys_role_4cdf1232` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_sys_user_sys_user_cef66251` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `sys_menu` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `name` VARCHAR(20)   COMMENT '名称',
    `icon` VARCHAR(100)   COMMENT '菜单图标',
    `path` VARCHAR(128)   COMMENT '菜单url',
    `type` SMALLINT NOT NULL  COMMENT '菜单类型 0目录 1组件 2按钮 3数据',
    `component` VARCHAR(128)   COMMENT '组件地址',
    `pid` INT   COMMENT '父id',
    `identifier` VARCHAR(30)   COMMENT '权限标识 user:add',
    `api` VARCHAR(128)   COMMENT '接口地址',
    `method` VARCHAR(10)   COMMENT '接口请求方式',
    KEY `idx_sys_menu_type_a01aeb` (`type`, `name`)
) CHARACTER SET utf8mb4 COMMENT='菜单表';
CREATE TABLE IF NOT EXISTS `sys_role_menu` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `status` SMALLINT NOT NULL  COMMENT '状态 1有效 9 删除 5选中' DEFAULT 1,
    `created` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `modified` DATETIME(6)   COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `menu_id` INT NOT NULL,
    `role_id` INT NOT NULL,
    CONSTRAINT `fk_sys_role_sys_menu_a6b431d9` FOREIGN KEY (`menu_id`) REFERENCES `sys_menu` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_sys_role_sys_role_077af6b8` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
