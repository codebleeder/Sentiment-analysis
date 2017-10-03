register /usr/lib/pig/piggybank.jar;

data = load '../totalData/' as (date:chararray, sentence:chararray, polarity: float, subjectivity: float);
stats = foreach data generate date, polarity, subjectivity;
sameDate = group stats by date;
--dump sameDate;
describe stats;
--store stats into 'stats';
objective = filter stats by subjectivity<0.5;
store objective into 'objective';