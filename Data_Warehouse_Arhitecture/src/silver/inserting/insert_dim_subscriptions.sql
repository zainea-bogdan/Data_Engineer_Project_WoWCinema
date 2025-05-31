insert into silver_wowcinema.dim_subscriptions
  select distinct bsp.*,
				  case
					 when bsp.subscription_plan_id = 1 then
						15
					 when bsp.subscription_plan_id = 2 then
						30
					 when bsp.subscription_plan_id = 3 then
						45
					 else
						0
				  end
	from bronze_wowcinema.subscription_plan bsp
	ON CONFLIct DO NOTHING;