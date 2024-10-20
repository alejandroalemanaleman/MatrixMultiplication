#!/bin/bash

matrix_sizes=(10 100 500 1000)
rounds=5  
iterations=3  

output_file="benchmark_results.csv"

echo "Matrix Size;Round;Iteration; TimeElapsed(sec); Maximum RSS (kbytes)" > $output_file

for size in "${matrix_sizes[@]}"; do
    echo "Running for matrix size: $size"
    
    for round in $(seq 1 $rounds); do
        echo "  Round $round"
        
        for iter in $(seq 1 $iterations); do
            echo "    Iteration $iter"

            perf_result=$(perf stat -e task-clock ./matriz $size 2>&1)
                       
            execution_time_ms=$(echo "$perf_result" | awk -F',' '{print $1}')
            execution_time_sec=$(echo "$perf_result" | grep "seconds time elapsed" | awk '{print $1}')

            time_result=$(/usr/bin/time -v ./matriz $size 2>&1)

            max_rss=$(echo "$time_result" | grep "Maximum resident set size" | awk '{print $6}')
                        
            if [ -n "$execution_time_sec" ] && [ -n "$max_rss" ]; then

                echo "$size;$round;$iter;$execution_time_sec;$max_rss" >> $output_file
            else
                echo "Error in with size: $size, round: $round, iteration: $iter"
            fi
        done
    done
done

echo "Benchmarks stored."




