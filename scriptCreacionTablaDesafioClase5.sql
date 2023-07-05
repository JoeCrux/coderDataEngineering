create table company_earnings(
		actual decimal,
		estimate decimal,
		periodo date,
		cuarto int,
		surprise decimal,
		surprisePercent decimal,
		symbol varchar(15) DISTKEY,   
		anio int 
	) SORTKEY (anio)
