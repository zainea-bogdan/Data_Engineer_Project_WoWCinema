insert into silver_wowcinema.dim_reactions
values(1,'like')
on conflict do nothing;

insert into silver_wowcinema.dim_reactions
values(-1,'dislike')
on conflict do nothing;

insert into silver_wowcinema.dim_reactions
values(0,'neutral')
on conflict do nothing;