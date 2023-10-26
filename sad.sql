create database Nintendo_Games char set utf8mb4 collate utf8mb4_unicode_ci;
use Nintendo_Games;

create table Games(
game_index int auto_increment primary key,
game_title varchar(150) not null,
platform varchar(100) not null,
release_date varchar(100) not null,
esrb_rating varchar(10) not null,
genre varchar(250) not null,
devs varchar(150) not null
);

create table Score(
user_score varchar(3),
meta_score varchar(3),
game_index int auto_increment,
constraint foreign key (game_index) references Games(game_index)
);

select * from Games;
select * from Score;

select Games.*, Score.user_score, Score.meta_score from Games inner join Score on Games.game_index = Score.game_index;




