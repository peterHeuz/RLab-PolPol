#!/bin/bash

echo reading articles-training-byarticle-20181122.xml ...
python read_article_data.py articles-training-byarticle-20181122

echo reading articles-training-bypublisher-20181122.xml ...
python read_article_data.py articles-training-bypublisher-20181122

echo reading articles-validation-bypublisher-20181122.xml ...
python read_article_data.py articles-validation-bypublisher-20181122

echo reading ground-truth-training-byarticle-20181122.xml ...
python read_gt_byart.py ground-truth-training-byarticle-20181122

echo reading ground-truth-training-bypublisher-20181122.xml ...
python read_gt_bypub.py ground-truth-training-bypublisher-20181122

echo reading ground-truth-validation-bypublisher-20181122.xml ...
python read_gt_bypub.py ground-truth-validation-bypublisher-20181122