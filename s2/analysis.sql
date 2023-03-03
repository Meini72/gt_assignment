select
	a.member_id,
	a.name,
	sum(b.total_item_price) as total_spending
from member a
left join (
	select
		order_id,
		item_id,
		member_id,
		total_item_price,
		order_date
	from order_table
	where order_date>date_sub(now(), interval '30' day)
) b
on a.member_id=b.member_id
group by a.member_id, a.name
order by total_spending desc
limit 10;



select
	a.item_id,
	a.item_name,
	count(b.order_id) as cnt_txn
from item a
left join (
	select
		order_id,
		item_id
	from order_table
	where order_date>date_sub(now(), interval '30' day)
) b
on a.item_id=b.item_id
group by a.item_id, a.item_name
order by cnt_txn desc
limit 3
;