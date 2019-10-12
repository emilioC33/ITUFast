// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "EvaluationState.generated.h"

/**
 * 
 */
UENUM(BlueprintType)
enum class EEvaluationState : uint8
{
	Ready			UMETA(DisplayName = "Ready"),
	Evaluating		UMETA(DisplayName = "Evaluating"),
	Done			UMETA(DisplayName = "Done")
};
