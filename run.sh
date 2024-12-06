#!/bin/bash
#SBATCH -J classifierTrainer_4GPUs
#SBATCH -o myjob_4GPUs_%j.out
#SBATCH -e myjob_4GPUs_%j.err
#SBATCH --gres=gpu:4
#SBATCH --gpus-per-node=4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=0
#SBATCH --time=9:33:33
#SBATCH --exclusive

module load anaconda3/2020.02-2ks5tch
module load cuda/11.8

#activate environment
source /home/paulg9/miniforge3/bin/activate

srun /home/paulg9/miniforge3/bin/python run_clm.py \
    --model_type gpt2 \
    --dataset_name chaseharmon/6.7960_FINAL \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --do_train \
    --do_eval \
    --output_dir /tmp/test-clm \
    --overwrite_output_dir True \
    --num_train_epochs 100 \
    --fp16 
